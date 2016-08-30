#  PokemonGo Device List Repository
A repository of pokemon-go device info and other material

The purpose of this repository is to create a database of information reported by the Pokemon Go client - grouped primarily by device. This will provide insight on what is transmitted by the client and will also allow 3rd party to emulate any device consistently.

## File format 
  The database is JSON formatted  and contains the following information:
  * device_info contents 
  * Available MEMS and magnetic sensors and capabilities
    - Number of axes 
    - Typical range of values during use
  * The general family of the device : currently android or iOS
  * Gps capabilities
    - GPS or GLONASS
    - SNR ranges (0 = not reported)

## Contributing

Create a pull-request or an issue on the issue tracker with ALL the required information. Incomplete reportings are not good enough.

## Core Maintainers

* [vosk](https://github.com/vosk)
