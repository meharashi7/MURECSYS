#!/usr/bin/env python
# coding: utf-8

# In[2]:


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f9e4caabe78b423a9fa2ca7d69d0f79a",
                                                           client_secret="ca2ed593ea874ee09b9d3123087c7076"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])


# In[ ]:




