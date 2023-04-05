## user/best19

| arguments    | description                                                                      | optional                                        |
|:-------------|:---------------------------------------------------------------------------------|-------------------------------------------------|
| SessionToken | SessionToken provided by TapTap                                                  | false                                           |
| songid       | string, commonly like 'Rrharil.TeamGrimoire.0' ('songname.composername.0')       | false                                           |
| level        | string, among ["EZ", "HD", "IN", "AT", "Legacy"], default = "IN"                 | true                                            |
| withsonginfo | boolean. if true, will reply with songinfo, default = false                      | true                                            |

###### Tag

* Need Token

#### Example

+ `{apiurl}/user/best?SessionToken={token}&level=HD&songid=Spasmodic.姜米條颶風元力上人.0&withsonginfo=true`

#### Specially

* If the songid or level fields are invalid or the difficulty level of the song has not been played, the return data will be like

```json5
{
  "status": false,
  "content": "Invalid songid or level"
}
```

###### Return data (Edited for readability)

```json5
{
  "status": true,
  "content": {
    "RankingScore": 15.35472297668457,
    "ChallengeModeRank": 445,
    "PlayerID": "yuhao7370",
    "record": {
      "songid": "Spasmodic.姜米條颶風元力上人.0",
      "level": "HD",
      "songname": "Spasmodic",
      "rating": 12.6,
      "rks": 12.6,
      "score": 1000000,
      "acc": 100,
      "isfc": true
    },
    "songinfo": {
      "songid": "Spasmodic.姜米條颶風元力上人.0",
      "level": "HD",
      "chartDetail": {
        "rating": 12.6,
        "charter": "無極☆雷鳴 ~ ♫死の序曲♫",
        "numOfNotes": 904
      },
      "chapterCode": "MainStory5",
      "unlockType": 4,
      "songsName": "Spasmodic",
      "composer": "姜米條☆颶風 ~ ♫元力上人♫",
      "illustrator": "昔璃☆暴雨 ~ ♫危難聖帝♫"
    }
  }
}
```
