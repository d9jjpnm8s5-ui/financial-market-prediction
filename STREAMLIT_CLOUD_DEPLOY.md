# Streamlit Community Cloud Deployment Guide

## Current Status
✅ App is running locally on `http://127.0.0.1:8501`  
✅ Entry point: `app/dashboard.py` (at repository root)  
✅ Dependencies optimized for Streamlit Cloud  
✅ Repository synced with GitHub  

## Quick Deployment Steps

### Step 1: Push to GitHub
All changes are automatically saved to `https://github.com/naman00008/financial-market-prediction`

```bash
cd /Users/namanvyas/Desktop/sentiment\ analysis
git status
git add -A
git commit -m "Prepare for Streamlit Cloud deployment"
git push origin main
```

### Step 2: Deploy via Streamlit Community Cloud
1. Visit https://share.streamlit.io
2. Sign in with your GitHub account
3. Click **"New app"**
4. Configuration:
   - **Repository:** `naman00008/financial-market-prediction`
   - **Branch:** `main`
   - **Main file path:** `app/dashboard.py`
5. Click **"Deploy"**

### Step 3: Monitor Deployment
- Build typically takes 2-5 minutes
- Check logs for any import or data file errors
- Once green, app will be live at: `https://financial-market-prediction.streamlit.app`

## Environment Variables (if needed)
If your app requires environment variables, add them in Streamlit Cloud dashboard:
- Settings > Secrets
- Add any required API keys or configuration

## Troubleshooting

### Import Errors
If modules are missing:
- Verify all imports are listed in `requirements.txt`
- Restart the app from Streamlit Cloud menu

### Data Files Not Found
Local CSV files are included in the repo. If still missing:
- Ensure `NSE-Data-main/` and `NSE-stock-market-historical-data-main/` are committed
- Check `src/data_preprocessing.py` for correct relative paths

### Slow Load Times
First cold start may take 30-60 seconds on Streamlit Cloud (limited resources).

## Features Included
- **Live Stock Data:** Real-time data via Yahoo Finance
- **Sentiment Analysis:** VADER sentiment on news feeds
- **Market Events:** Company-scoped corporate actions and events
- **Predictions:** 6-horizon stock price forecasts (1D, 1W, 1M, 3M, 6M, 1Y)
- **Portfolio Analysis:** Multi-stock risk-return analysis
- **Charts:** Interactive Plotly visualizations

## Auto-Deploy on Push
After initial setup, any push to `main` will trigger automatic redeployment!

## Support Resources
- Streamlit Cloud docs: https://docs.streamlit.io/streamlit-cloud
- GitHub repo: https://github.com/naman00008/financial-market-prediction
- Streamlit community: https://discuss.streamlit.io
