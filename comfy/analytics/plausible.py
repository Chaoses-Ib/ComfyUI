import asyncio
import json

import aiohttp
from typing import Optional, Dict, Any, Union

from .event_tracker import EventTracker


class PlausibleTracker(EventTracker):
    def __init__(self, loop: asyncio.AbstractEventLoop, user_agent: str, base_url: str, domain: str) -> None:
        super().__init__()
        self._user_agent = user_agent
        self._domain = domain
        self._base_url = base_url
        self.loop = loop
        self.session = aiohttp.ClientSession(loop=self.loop)

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str) -> None:
        self._user_agent = value

    @property
    def domain(self) -> str:
        return self._domain

    @domain.setter
    def domain(self, value: str) -> None:
        self._domain = value

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str) -> None:
        self._base_url = value

    async def track_event(self, name: str, url: str, referrer: Optional[str] = None,
                          props: Optional[Dict[str, Any]] = None) -> str:
        headers = {
            'User-Agent': self.user_agent,
            'Content-Type': 'application/json'
        }
        data = {
            'name': name,
            'url': url,
            'domain': self.domain
        }
        if referrer:
            data['referrer'] = referrer
        if props:
            data['props'] = props

        async with self.session.post(f'{self.base_url}/api/event', headers=headers,
                                     data=json.dumps(data)) as response:
            return await response.text()

    async def close(self) -> None:
        await self.session.close()
