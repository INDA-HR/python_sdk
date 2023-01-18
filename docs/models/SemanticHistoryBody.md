# inda_hr.model.semantic_history_body.SemanticHistoryBody

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[APICalls](#APICalls)** | list, tuple,  | tuple,  | Optional. List of events whose history data has to be returned. | [optional] 
**Datetime** | [**DateBody**](DateBody.md) | [**DateBody**](DateBody.md) |  | [optional] 
**[GroupBy](#GroupBy)** | list, tuple,  | tuple,  | Optional. List of terms according to which history data has to be aggregated. The allowed terms are *advanced* and *api_calls*; the aggregtion order is the same of the list items. A *Count* value is returned for each aggregation, as well as a *Prices* value if *Price* is set to *true*. | [optional] 
**ScrollID** | str,  | str,  | Optional. A scroll ID is provided if more data is available; this ID has to be passed in the next request to get further data. | [optional] 
**Detail** | bool,  | BoolClass,  | Optional. If *false*, just the count of the events respecting the filters is returned. Please note that if *Detail* is *true* and the *GroupBy* filter is used, just the last 100 events are provided. | [optional] if omitted the server will use the default value of True
**Advanced** | bool,  | BoolClass,  | Optional. According to its value, *true* or *false* respectively, just the *advanced* or *not advanced* events are taken into account for the response. If not set, events related to both types are returned. | [optional] 
**Price** | bool,  | BoolClass,  | Optional. If *true*, the total amount of credits spent per each service is returned. Please note that these values are returned in a *Prices* section if *GroupBy* is not set, otherwise they are injected in the *GroupBy* response. | [optional] if omitted the server will use the default value of True

# APICalls

Optional. List of events whose history data has to be returned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Optional. List of events whose history data has to be returned. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# GroupBy

Optional. List of terms according to which history data has to be aggregated. The allowed terms are *advanced* and *api_calls*; the aggregtion order is the same of the list items. A *Count* value is returned for each aggregation, as well as a *Prices* value if *Price* is set to *true*.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Optional. List of terms according to which history data has to be aggregated. The allowed terms are *advanced* and *api_calls*; the aggregtion order is the same of the list items. A *Count* value is returned for each aggregation, as well as a *Prices* value if *Price* is set to *true*. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

