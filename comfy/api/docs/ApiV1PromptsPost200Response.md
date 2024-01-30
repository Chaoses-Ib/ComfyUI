# ApiV1PromptsPost200Response

A list of URLs to retrieve the binary content of the image.  This will return two URLs. The first is the ordinary ComfyUI view image URL that exactly corresponds to the UI call. The second is the URL that corresponds to sha256 hash of the request body.  Hashing function for web browsers:  ```js async function generateHash(body) {   // Stringify and sort keys in the JSON object   let str = JSON.stringify(body);    // Encode the string as a Uint8Array   let encoder = new TextEncoder();   let data = encoder.encode(str);    // Create a SHA-256 hash of the data   let hash = await window.crypto.subtle.digest('SHA-256', data);    // Convert the hash (which is an ArrayBuffer) to a hex string   let hashArray = Array.from(new Uint8Array(hash));   let hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');    return hashHex; } ```  Hashing function for nodejs:  ```js const crypto = require('crypto');  function generateHash(body) {   // Stringify and sort keys in the JSON object   let str = JSON.stringify(body);    // Create a SHA-256 hash of the string   let hash = crypto.createHash('sha256');   hash.update(str);    // Return the hexadecimal representation of the hash   return hash.digest('hex'); } ```  Hashing function for python: ```python def digest(data: dict | str) -> str:   json_str = data if isinstance(data, str) else json.dumps(data, separators=(',', ':'))   json_bytes = json_str.encode('utf-8')   hash_object = hashlib.sha256(json_bytes)   return hash_object.hexdigest()  ``` 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** |  | [optional] 

## Example

```python
from comfy.api.models.api_v1_prompts_post200_response import ApiV1PromptsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PromptsPost200Response from a JSON string
api_v1_prompts_post200_response_instance = ApiV1PromptsPost200Response.from_json(json)
# print the JSON string representation of the object
print ApiV1PromptsPost200Response.to_json()

# convert the object into a dict
api_v1_prompts_post200_response_dict = api_v1_prompts_post200_response_instance.to_dict()
# create an instance of ApiV1PromptsPost200Response from a dict
api_v1_prompts_post200_response_form_dict = api_v1_prompts_post200_response.from_dict(api_v1_prompts_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


