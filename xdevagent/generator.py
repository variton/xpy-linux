#! /usr/bin/python3

from openai import OpenAI

import os
import sys
import asyncio

PDOCUMENTATION = {"role": "developer", 
                  "content": f"Only complete the code with the sphinx docstring doc like \
                   and example for the following code. Respect the 79 characters long on a line \n {}".format(code)}

PUT = {"role": "developer", 
               "content": "Only generate unit tests runable with pytest and \
                do not gegenerate any test with unittest.mock \
                for the following \n {}".format(code)}

class ModelHdr:
    def __init__(self, _model_name) -> None:
        self.model_name_ = _model_name
        self.client_ = OpenAI(api_key=os.environ['OPEN_AI_KEY'])

    def task(self,prompt:dict) -> object: 
    
        response = self.client_.chat.completions.create(
            model=self.model_name_,
            messages=[prompt])

        obj = response.choices[0].message.content
    
    def get_documentation(code:str,filename:str) -> None:
        self.task(PDOCUMENTATION)

async def get_documentation(code:str,filename:str) -> str:

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "developer", 
             "content": f"Only complete the code with the sphinx docstring doc like \
              and example for the following code. Respect the 79 characters long on a line \n {code}"}]
    )

    documentation = response.choices[0].message.content
    with open(f"{filename}", "w", encoding="utf-8") as f:
        f.write(documentation)
    print("finished generating the documentation")

async def get_unit_test(code:str,filename:str) -> str:

    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "developer", 
             "content": f"Only generate unit tests runable with pytest and \
             do not gegenerate any test with unittest.mock \
             for the following {code}.\n {code}"}]
    )

    ut = response.choices[0].message.content
    with open(f"test_{filename}", "w", encoding="utf-8") as f:
        f.write(ut)
    print("finished generating the unit tests")

async def run(code:str,filename:str) :
    await get_documentation(code,filename)
    await get_unit_test(code,filename)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('missing argument')
        print('example: generator code.py')
        sys.exit(1)

    codefpath = sys.argv[1]

    file=None
    for element in sys.argv:
        if "-p" in element:
            file=element.replace("-p=","")

    codefpath=file
    with open(codefpath, "r") as f:
        code = f.read()
        asyncio.run(run(code,codefpath))
