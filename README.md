# GameDB-GB
Nintendo Game Boy (GB), part of [GameDB](https://github.com/niemasd/GameDB).

## Structured Downloads
* **[`GB.data.json`](https://github.com/niemasd/GameDB-GB/releases/latest/download/GB.data.json):** All data, structured in the JSON format
* **[`GB.data.tsv`](https://github.com/niemasd/GameDB-GB/releases/latest/download/GB.data.tsv):** All data, structured in the TSV format
* **[`GB.release_dates.pdf`](https://github.com/niemasd/GameDB-GB/releases/latest/download/GB.release_dates.pdf):** Histogram of release dates, stratified by region
* **[`GB.titles.json`](https://github.com/niemasd/GameDB-GB/releases/latest/download/GB.titles.json):** Mapping of serial numbers to game titles, structured in the JSON format

# Notes

## Uniquely Identifying Games

GB games don't have unique internal game IDs or serial numbers. The following 2 fields can be used to uniquely identify a game:

1. The **Internal Title**, which is at offsets `0x0134` through `0x013E/0x0143` (inclusive) of the [ROM header](https://github.com/niemasd/GameDB-GB/wiki#memory-map)
2. The **Global Checksum**, which is at offsets `0x014E` through `0x014F` (inclusive) of the [ROM header](https://github.com/niemasd/GameDB-GB/wiki#memory-map)

The game folders within [`games`](games) are named as follows (i.e., these 2 fields delimited by `.....`):

```
INTERNAL_TITLE.....GLOBAL_CHECKSUM
```

* Whitespace in the internal title is stripped
* Special characters in the internal title are replaced with `_`

# Sources
* [No-Intro](https://no-intro.org/)
