# Usage

## ApiBase

Main class object `PhishlabsApi` contains the following methods.

### \_\_init\_\_

Initialize the API.

Built-in method; requires no configuration.

### \_\_exit\_\_

Built-in method; requires no configuration.

### pl_process_params --> list

Process parameters to Phishlabs query into correct format.

#### Parameters

<pre>

	<b>**kwargs</b> : dict
	
	Possible Phishlabs parameters.
	
	Options:
	
        case_type; default = ['Phishing', 'Phishing Redirect', 'Vishing']
        date_begin; default = None
        date_end; default = None
        date_field; default = 'caseOpen'
        format; default = json
        max_records; default = 100
        offset; default = 0
        [custom]; default = None; filter on any Phishlabs case field
                Ex. 'fieldName'='fieldData
	
</pre>

#### Returns

<pre>

	<b>list</b>
	
	Processed query parameters.
	
</pre>

### *async* get_attachments --> dict

Get filenames of attachments to identified Phishlabs cases.

#### Parameters

<pre>

	<b>attachments</b> : Union[List[dict], dict]
	
	Phishlab case identifiers to query.
	
</pre>

#### Returns

<pre>

	<b>dict</b>
	
	Dictionary containing results of attachments query.
	
	Example {queryField : queryData, 'filePath' : 'resultFilePath'} 
	
</pre>

### *async* get_case --> dict

Get details pertaining to a specific Phishlabs case.

#### Parameters

<pre>

	<b>case_id</b> : str
	
	Case ID of Phishlab to be queried.
	
</pre>

#### Returns

<pre>

	<b>dict</b>
	
	Dictionary containing results of case query -- case details if success, 
	                                                    otherwise note of failure.
	
</pre>

### *async* get_case_count --> int

Get details pertaining to a specific Phishlabs case.

#### Parameters

<pre>

	<b>**kwargs</b> : dict 
	
	(Optional)
	
	Optional parameters to send with Phishlabs query.
	
</pre>

See [pl_process_params](#pl_process_params-dict) for options.

#### Returns

<pre>

	<b>int</b>
	
	Number of Phishlabs cases.
	
</pre>

### *async* get_case --> dict

Get details pertaining to all Phishlabs cases.

#### Parameters

<pre>

	<b>**kwargs</b> : dict 
	
	(Optional)
	
	Optional parameters to send with Phishlabs query. 
	
</pre>

See [pl_process_params](#pl_process_params-dict) for options.

#### Returns

<pre>

	<b>dict</b>
	
	Dictionary containing results of case queries.
	
</pre>
