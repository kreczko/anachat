# hepbot
A chat bot for Slack based on [slackbot](https://github.com/lins05/slackbot) to interface with projects based on [hepshell](https://github.com/kreczko/hepshell).

To run the bot you need to setup your API_TOKEN (from slack) as a variable:
```bash
API_TOKEN=<>; export API_TOKEN
# and then launch the bot:
python hepbot/run.py
```

If you also with to add custom responses, please add the python package or module to
```bash
PLUGINS=<comma separated list>
```
On how to construct these repsonses, please have a look at [slackbot examples](https://github.com/lins05/slackbot/tree/develop/slackbot/plugins).

# hepbot in docker
Alternatively you can start the hepbot in a docker container:
```bash
docker run -e "API_TOKEN=<>" -d --name hepbot -t kreczko/hepbot
# to stop
docker stop hepbot
# to start again
docker start hepbot
```

