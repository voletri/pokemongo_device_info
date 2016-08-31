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

#Example 
```
"devicename" :
    {
        "platform" : "value reported in DownloadRemoteConfigVersion",
        "device_info":
        {
            "device_id" : "DONT include this one",
            "android_board_name": "as reported",
            "android_bootloader": "as reported",
            "device_brand": "as reported",
            "device_model": "as reported",
            "device_model_identifier": "as reported",
            "device_model_boot": "as reported",
            "hardware_manufacturer": "as reported",
            "hardware_model": "as reported",
            "firmware_brand": "as reported",
            "firmware_tags": "as reported",
            "firmware_type": "as reported",
            "firmware_fingerprint": "as reported"
        },
        "is_android" : true,
        "is_ios" : false,
        
        "has_android_gps_info" : true, == reports android_gps_info
        "android_gps_info" : 
        {
            "gps_snr_range" : [0, 46], == min and max reported snr
            "gps_has_glonass" : true, ==Device capabilites : PRN`s >64 means it has glonass
            "gps_has_gps" : true,  ==Device capabilites : PRN`s <64 means it has gps
        },
        "has_sensor_update" : false,  == reports sensor_udpate
        "sensor_update" :
        {
            "acc_axes_availability" : [false, false, false ], ==X/Y/Z availability
             "magn_axes_availability" : [false, false, false ],==X/Y/Z availability
            "mang_field_accuracy_availability" : false, == TODO
            "att_axes_availability" : [ false,false, false ], ==TODO
            "rot_axes_availability" : [ false,false, false ], ==TODO
            "gravity_axes_availability" : [ false,false, false ], ==TODO
            "sensor_info_status" : false == TODO
        },
        "has_location_update" : true,
        "location_update" :
        {
            "gps" : == Normally location_update.name
            {
            "report" : "gps" , ==Name reported
            "has_valid" : true, == update can have valid gps coords
            "invalid_altitude" : true, == Report altitude when coords invalid
            "invalid_latitude" : 360, == What values are reported when invalid
            "invalid_longitude" : 360, == What values are reported when invalid
            "invalid_provider_status" : 3, ==when coords invalid
            "valid_altitude" :true, ==Report altitude when coords valid
            "valid_provider_status": 3, =when coords valid 
            "invalid_horizontal_accuracy" : 52, ==Horizontal accuracy when invalid coords are reported
            "valid_horizontal_accuracy" : [5, 67], == Min max range
            "rounded" : ["horizontal_accuracy","altitude"] ==At least my device seems to round these
            },
            "network" : ==Same as above
            {
            "report" : "network",
            "has_valid" : false, 
            "invalid_altitude" : false,
            "invalid_latitude" : 360,
            "invalid_longitude" : 360,
            "invalid_provider_status" : 3,            
            "invalid_horizontal_accuracy" : 25
            }
        },
        "has_ios_device_info" : false,
        "ios_device_info": {  }  == TODO
    }

```


## Contributing

Create a pull-request or an issue on the issue tracker with ALL the required information. Incomplete reportings are not good enough.

## Core Maintainers

* [vosk](https://github.com/vosk)
