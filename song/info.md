## song/info

| arguments    | description                                                                      | optional                                        |
|:-------------|:---------------------------------------------------------------------------------|-------------------------------------------------|
| songid       | string, commonly like 'Rrharil.TeamGrimoire.0' ('songname.composername.0')       | false                                           |


#### Example

+ `{apiurl}/song/info?songid=Random.SobremSilentroom.0`

#### Specially

* If the songid field is invalid, the return data will be like

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
    "songid": "Random.SobremSilentroom.0",
    "info": {
      "chapterCode": "Single",
      "unlockType": 1,
      "songsName": "Random",
      "composer": "Sobrem × Silentroom",
      "illustrator": "Harkiadel",
      "chartDetail": {
        "level_list": [
          "EZ",
          "HD",
          "IN"
        ],
        "EZ": {
          "rating": 6,
          "charter": "Barbarianerman",
          "numOfNotes": 275
        },
        "HD": {
          "rating": 11.1,
          "charter": "IMD_6",
          "numOfNotes": 568
        },
        "IN": {
          "rating": 14.7,
          "charter": "_鉄",
          "numOfNotes": 732
        }
      }
    }
  }
}
```
