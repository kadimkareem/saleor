import asyncio
import aiohttp
import json
import aiofiles
from common import get_github_access_token

issues_url = 'https://api.github.com/repos/saleor/saleor/issues'
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {get_github_access_token()}"
}

async def fetch_issues(session, page):
    params = {
        "state": "all",  # Fetch both open and closed issues
        "per_page": 100,
        "page": page,
        "sort": "created",
        "direction": "desc"  # Fetch the latest issues first
    }
    async with session.get(url=issues_url, headers=headers, ssl=False, params=params) as response:
        if response.status == 200:
            return await response.json()
        else:
            print(f"Failed to fetch data for page {page}: {response.status}")
            return []

async def fetch_all_issues():
    '''because github limitation to fetch only 100 issue per page '''
    all_issues = []
    async with aiohttp.ClientSession() as session:
        page = 1
        while len(all_issues) < 500:
            issues = await fetch_issues(session, page)
            if not issues:
                break  # No more issues to fetch
            all_issues.extend(issues)
            page += 1
            # If we have reached 500 issues, truncate the list
            if len(all_issues) >= 500:
                all_issues = all_issues[:500]
                break
    return all_issues

async def save_json(data):
    if data:
        async with aiofiles.open('./outputs/issues_json.json', 'w') as file:
            await file.write(json.dumps(data, indent=4))
        print("Data saved to issues_json.json")
    else:
        print("No data to save.")

async def main():
    issues_data = await fetch_all_issues()
    if issues_data:
        await save_json(issues_data)

if __name__ == '__main__':
    asyncio.run(main())