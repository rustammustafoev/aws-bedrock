import os

import requests


def scrape_linkedin_profile(profile_url: str):
    """Scrape LinkedIn profile information"""

    response = requests.get(
        url="https://nubela.co/proxycurl/api/v2/linkedin",
        params={"url": profile_url},
        headers={"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k
        not in [
            "people_also_viewed",
            "certifications",
            "accomplishment_publications",
            "accomplishment_honors_awards",
            "accomplishment_projects",
        ]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
