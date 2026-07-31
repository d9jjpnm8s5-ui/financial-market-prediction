# Stock Market Analysis Platform - Deployment Guide

## Production Deployment

### Prerequisites
- Python 3.10+
- pip or conda
- Virtual environment (recommended)

### Local Development Setup

```bash
# Clone or navigate to project directory
cd stock_market_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download required NLTK data
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"

# Run the application
streamlit run app/dashboard.py
```

### Docker Deployment

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

Build and run:

```bash
docker build -t stock-market-app .
docker run -p 8501:8501 stock-market-app
```

### Cloud Deployment (Heroku)

1. Create `Procfile`:
```
web: streamlit run app/dashboard.py --server.port=$PORT --server.address=0.0.0.0
```

2. Create `.streamlit/config.toml` for production:
```toml
[server]
maxUploadSize = 200
enableCORS = false
headless = true

[client]
showErrorDetails = false
```

3. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
```

### Cloud Deployment (AWS Elastic Beanstalk)

1. Install AWS EB CLI
2. Initialize application:
```bash
eb init -p python-3.11 stock-market-app
```

3. Create and deploy:
```bash
eb create prod-env
eb deploy
```

### Environment Variables

Create `.env` file:
```
NEWS_API_KEY=your_newsapi_key_here
FLASK_ENV=production
DEBUG=False
```

## Performance Optimization

### Caching Strategy
- Stock data cached for 30 seconds (live updates)
- News data cached for 5 minutes
- Technical indicators computed once per session
- ML models cached after first training

### Database Setup (Optional)
For production, consider adding database caching:

```python
# Use Redis for session caching
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Cache live data
cache_key = f"stock:{ticker}:{period}"
cached_data = redis_client.get(cache_key)
```

## Security Considerations

1. **API Keys**: Store in environment variables, never commit to git
2. **HTTPS**: Enable in production
3. **Rate Limiting**: Implement request throttling
4. **CORS**: Configure properly for cross-domain requests
5. **Input Validation**: All user inputs are validated
6. **Error Handling**: Production errors logged, not displayed to users

## Monitoring & Logging

### Application Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)
```

### Performance Monitoring
- Track page load times
- Monitor data fetch latencies
- Alert on API failures
- Log model training times

## Scalability

### Multi-Instance Deployment
- Use load balancer (Nginx, HAProxy)
- Session state in Redis
- Shared model cache
- Connection pooling for databases

### Database Scaling
```sql
CREATE INDEX idx_stock_date ON stocks(ticker, date);
CREATE INDEX idx_news_company ON news(company, published_at);
```

## Troubleshooting

### Common Issues

**Issue**: News API rate limit exceeded
```
Solution: Increase cache duration, use fallback RSS feeds
```

**Issue**: Memory usage high on production
```
Solution: Implement model caching, limit DataFrame sizes, enable garbage collection
```

**Issue**: Slow chart rendering
```
Solution: Sample data for large date ranges, use WebGL for Plotly, optimize indicator calculations
```

## Maintenance

### Regular Tasks
- Monitor API usage and quotas
- Update dependencies monthly
- Review and optimize slow queries
- Clear old cache files
- Backup database and models

### Update Procedure
```bash
# Create backup
git checkout -b backup-prod

# Update dependencies
pip install -r requirements.txt --upgrade

# Run tests
pytest tests/

# Deploy
git push production main
```

## Support & Resources

- Streamlit Docs: https://docs.streamlit.io
- Plotly Reference: https://plotly.com/python/
- XGBoost Tutorials: https://xgboost.readthedocs.io
- yfinance Documentation: https://github.com/ranaroussi/yfinance

---

**Last Updated**: July 2026  
**Recommended Python Version**: 3.11+  
**Deployment Target**: Production-ready
