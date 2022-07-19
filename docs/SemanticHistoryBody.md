# SemanticHistoryBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_calls** | **[str]** | Optional. List of events whose history data has to be returned. | [optional] 
**datetime** | [**DateBody**](DateBody.md) |  | [optional] 
**group_by** | **[str]** | Optional. List of terms according to which history data has to be aggregated. The allowed terms are *advanced* and *api_calls*; the aggregtion order is the same of the list items. A *Count* value is returned for each aggregation, as well as a *Prices* value if *Price* is set to *true*. | [optional] 
**scroll_id** | **str** | Optional. A scroll ID is provided if more data is available; this ID has to be passed in the next request to get further data. | [optional] 
**detail** | **bool** | Optional. If *false*, just the count of the events respecting the filters is returned. Please note that if *Detail* is *true* and the *GroupBy* filter is used, just the last 100 events are provided. | [optional]  if omitted the server will use the default value of True
**advanced** | **bool** | Optional. According to its value, *true* or *false* respectively, just the *advanced* or *not advanced* events are taken into account for the response. If not set, events related to both types are returned. | [optional] 
**price** | **bool** | Optional. If *true*, the total amount of credits spent per each service is returned. Please note that these values are returned in a *Prices* section if *GroupBy* is not set, otherwise they are injected in the *GroupBy* response. | [optional]  if omitted the server will use the default value of True

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


