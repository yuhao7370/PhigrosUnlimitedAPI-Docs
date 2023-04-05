## user/best19

| arguments    | description                                                                      | optional                                        |
|:-------------|:---------------------------------------------------------------------------------|-------------------------------------------------|
| SessionToken | SessionToken provided by TapTap                                                  | false                                           |
| overflow     | number, range 0-40. The number of the	overflow records below the best19 minimum | true                                            |
| withsonginfo | boolean. if true, will reply with songinfo                                       | true                                            |

###### Tag

* Need Token

#### Example

+ `{apiurl}/user/best19?SessionToken={token}&overflow=0&withsonginfo=true`

#### Specially

* The "phi" field in the returned data represents whether the first record in the list is phi1

###### Return data (Edited for readability)

```json5
{
  "status": true,
  "content": {
    "RankingScore": 15.35472297668457,
    "ChallengeModeRank": 445,
    "PlayerID": "yuhao7370",
    "best_list": {
      "phi": true,
      "best": [
        {
          "songid": "YouaretheMiserable.tpazolite.0",
          "level": "AT",
          "songname": "You are the Miserable",
          "rating": 15.8,
          "rks": 15.8,
          "score": 1000000,
          "acc": 100,
          "isfc": true
        },
        {
          "songid": "YouaretheMiserable.tpazolite.0",
          "level": "AT",
          "songname": "You are the Miserable",
          "rating": 15.8,
          "rks": 15.8,
          "score": 1000000,
          "acc": 100,
          "isfc": true
        },
        {
          "songid": "DontNeverAround.HAMA.0",
          "level": "IN",
          "songname": "Don't Never Around",
          "rating": 15.6,
          "rks": 15.6,
          "score": 1000000,
          "acc": 100,
          "isfc": true
        }
      ]
    },
    "best_songinfo": [
      {
        "songid": "YouaretheMiserable.tpazolite.0",
        "level": "AT",
        "chartDetail": {
          "rating": 15.8,
          "charter": "Pat Brick Man Mr.C & Mr.B",
          "numOfNotes": 1344
        },
        "chapterCode": "Lanota",
        "unlockType": 0,
        "songsName": "You are the Miserable",
        "composer": "t+pazolite",
        "illustrator": "Lanota © Noxy Games Inc. "
      },
      {
        "songid": "YouaretheMiserable.tpazolite.0",
        "level": "AT",
        "chartDetail": {
          "rating": 15.8,
          "charter": "Pat Brick Man Mr.C & Mr.B",
          "numOfNotes": 1344
        },
        "chapterCode": "Lanota",
        "unlockType": 0,
        "songsName": "You are the Miserable",
        "composer": "t+pazolite",
        "illustrator": "Lanota © Noxy Games Inc. "
      },
      {
        "songid": "DontNeverAround.HAMA.0",
        "level": "IN",
        "chartDetail": {
          "rating": 15.6,
          "charter": "XMT小咩兔",
          "numOfNotes": 1028
        },
        "chapterCode": "KALPA",
        "unlockType": 0,
        "songsName": "Don't Never Around",
        "composer": "HAMA",
        "illustrator": "Arahosi"
      }
    ]
  }
}
```
