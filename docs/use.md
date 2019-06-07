# Usage

## ApiBase

Main class object `ApiBase` contains the following methods.

### \_\_init\_\_

Initialize the API.

#### Parameters

<pre>

	<b>root</b> : str

	Defines the root directory in which the script runs (optional) 
	
	default = script's home directory

</pre>

<pre>

	<b>sem</b> : int
	
	Defines the Semaphore value, the max number of asynchronous requests (optional)
	
	default = `1000`
	
</pre>

<pre>

	<b>parent</b> : str
	
	Defines the the parent directory where the script runs (optional)
	
	default = parent of script's home directory
	
</pre>
	

### \_\_enter\_\_

Built-in method; requires no configuration.

### \_\_exit\_\_

Built-in method; requires no configuration.


### *async* request_debug --> str

Return a string containing details of a returned HTTP request, used for debugging.

#### Parameters

<pre>

	<b>resp</b> : aio.ClientResponse
	
	HTTP request to be debugged.
	
</pre>

#### Returns

<pre>

	<b>str</b>
	
	HTTP request return details.
	
</pre>

### *async* process_results --> dict

Process results of HTTP request to extract response data into a dict of actual result data.

#### Parameters

<pre>

	<b>results</b> : List[Union[dict, aio.ClientResponse]]
	
	Unique list of all HTTP responses that are being asynchronously processed.
	
</pre>

<pre>

	<b>data_list</b> : str
	
	Key of the primary data list to be accessed.
	
</pre>

#### Returns

<pre>

	<b>dict</b>
	
	Dictionary containing data from all request results.
	
</pre>

#### Example

	I don't have one, but I think it would be beneficial here.

### process_params --> dict

Return a dictionary of custom parameters, omitting those set to None.

#### Parameters

<pre>

	<b>**kwargs</b> : dict
	
	A dictionary of custom parameters.
	
</pre>

#### Returns

<pre>

	<b>dict</b>
	
	Dictionary containing custom arguments, omitting those set to none.
	
</pre>

#### Example

	a = {'apples' : 3, 'bananas' : None, 'carrots': 0}
	
	b = process_params(a)
	
	print(b)
	
	>>> {'apples' : 3, 'carrots': 0}

## Utility

Util file `base_api_utils.py' contains the following methods.

### bprint --> NoReturn

Print a message with custom API banner.

#### Parameters

<pre>

	<b>message</b> : Any
	
	Message or value to be printed.
	
</pre>

#### Returns

<pre>

	<b>NoReturn</b>
	
	Message prints to terminal.
	
</pre>