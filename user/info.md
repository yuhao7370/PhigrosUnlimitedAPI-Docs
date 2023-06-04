## user/best

| arguments    | description                                                                      | optional                                        |
|:-------------|:---------------------------------------------------------------------------------|-------------------------------------------------|
| SessionToken | SessionToken provided by TapTap                                                  | false                                           |

###### Tag

* Need Token

#### Example

+ `{apiurl}/user/info?SessionToken={token}`

###### Return data (Edited for readability)

```json5
{
  "status": true,
  "content": {
    "RankingScore": 15.35472297668457,
    "ChallengeModeRank": 445,
    "PlayerID": "yuhao7370",
  }
}
```
