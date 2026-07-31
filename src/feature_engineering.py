import pandas as pd
try:
    import pandas_ta as ta
    PANDAS_TA_AVAILABLE = True
except ImportError:
    ta = None
    PANDAS_TA_AVAILABLE = False


def _rsi(series: pd.Series, length: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=length, min_periods=length).mean()
    avg_loss = loss.rolling(window=length, min_periods=length).mean()

    rs = avg_gain / (avg_loss + 1e-9)
    rsi = 100 - (100 / (1 + rs))
    return rsi


def _macd(series: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()

    macd_line = ema_fast - ema_slow
    macd_signal = macd_line.ewm(span=signal, adjust=False).mean()
    macd_hist = macd_line - macd_signal

    return pd.DataFrame(
        {
            "MACD_12_26_9": macd_line,
            "MACDs_12_26_9": macd_signal,
            "MACDh_12_26_9": macd_hist,
        }
    )


def _bollinger_bands(series: pd.Series, length: int = 20, std: float = 2.0):
    sma = series.rolling(window=length, min_periods=length).mean()
    rolling_std = series.rolling(window=length, min_periods=length).std()
    upper = sma + std * rolling_std
    lower = sma - std * rolling_std
    return pd.DataFrame(
        {
            f"BBM_{length}_{std}": sma,
            f"BBU_{length}_{std}": upper,
            f"BBL_{length}_{std}": lower,
        }
    )


def add_technical_indicators(df: pd.DataFrame, fillna: bool = True) -> pd.DataFrame:
    """Compute common technical indicators and attach them to the DataFrame."""
    df = df.copy()

    # Ensure we have a close column
    if "Close" not in df.columns:
        raise ValueError("DataFrame must contain a 'Close' column")

    # Basic moving averages
    df["SMA_20"] = df["Close"].rolling(window=20, min_periods=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50, min_periods=50).mean()
    df["EMA_20"] = df["Close"].ewm(span=20, adjust=False).mean()
    df["EMA_50"] = df["Close"].ewm(span=50, adjust=False).mean()

    # RSI (only add if pandas_ta not available to avoid duplication)
    if not PANDAS_TA_AVAILABLE:
        df["RSI_14"] = _rsi(df["Close"], length=14)

    # MACD (only add if pandas_ta not available to avoid duplication)
    if not PANDAS_TA_AVAILABLE:
        macd = _macd(df["Close"], fast=12, slow=26, signal=9)
        df = pd.concat([df, macd], axis=1)

    # Bollinger Bands (only add if pandas_ta not available to avoid duplication)
    if not PANDAS_TA_AVAILABLE:
        bbands = _bollinger_bands(df["Close"], length=20, std=2)
        df = pd.concat([df, bbands], axis=1)

    # Additional indicators using pandas-ta
    if PANDAS_TA_AVAILABLE:
        try:
            # RSI using pandas-ta
            rsi_result = ta.rsi(df["Close"], length=14)
            if rsi_result is not None:
                df["RSI_14"] = rsi_result

            # MACD using pandas-ta
            macd_ta = ta.macd(df["Close"], fast=12, slow=26, signal=9)
            if macd_ta is not None:
                # Ensure no column name conflicts
                macd_ta_cols = macd_ta.columns.tolist()
                for col in macd_ta_cols:
                    if col not in df.columns:
                        df[col] = macd_ta[col]

            # Bollinger Bands using pandas-ta
            bb_ta = ta.bbands(df["Close"], length=20, std=2)
            if bb_ta is not None:
                bb_ta_cols = bb_ta.columns.tolist()
                for col in bb_ta_cols:
                    if col not in df.columns:
                        df[col] = bb_ta[col]

            # Stochastic Oscillator
            stoch = ta.stoch(df["High"], df["Low"], df["Close"])
            if stoch is not None:
                stoch_cols = stoch.columns.tolist()
                for col in stoch_cols:
                    if col not in df.columns:
                        df[col] = stoch[col]

            # Williams %R
            willr = ta.willr(df["High"], df["Low"], df["Close"])
            if willr is not None and "WILLR_14" not in df.columns:
                df["WILLR_14"] = willr

            # Commodity Channel Index
            cci = ta.cci(df["High"], df["Low"], df["Close"])
            if cci is not None and "CCI_14" not in df.columns:
                df["CCI_14"] = cci

            # Average True Range
            atr = ta.atr(df["High"], df["Low"], df["Close"])
            if atr is not None and "ATR_14" not in df.columns:
                df["ATR_14"] = atr

        except Exception as e:
            # If pandas-ta fails, continue with basic indicators
            pass

    if fillna:
        # `NDFrame.fillna(method=...)` may not be supported in all pandas versions,
        # so use the explicit `ffill`/`bfill` helpers to ensure compatibility.
        df = df.ffill().bfill()

    # Remove any remaining duplicate columns
    df = df.loc[:, ~df.columns.duplicated(keep='first')]

    return df


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """Generate a feature set for machine learning models."""
    df = df.copy()
    df = add_technical_indicators(df)

    # Create lagged returns features
    df["Return_1d"] = df["Close"].pct_change(1)
    df["Return_3d"] = df["Close"].pct_change(3)
    df["Return_5d"] = df["Close"].pct_change(5)

    # Drop NA rows created by shifting
    df = df.dropna().reset_index(drop=True)
    return df
