 - hepbot needs to know how to handle certificates: @hepbot take my cert from <host>:<path>
 - needs to create a slackbot_settings.py in PYTHONPATH from a param it gets
   - to defined API_TOKEN (secret)
   - to add the plugin module which defines the bot behaviour
 - docker container needs access to CVMFS
 - hepbot needs to be able to execute commands as a specific user (not root)
 - needs a map of chat names to user names or cert names to user names
 