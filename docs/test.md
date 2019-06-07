# Testing

Tests are located in project directory folder `./sealib_base/tests`.

## Instructions

### Development
Select Folder

    cd /sea
    
Clone Source

    git clone -b devl git@github.info53.com:Fifth-Third/sea_lib_base.git

Virtual Environment Setup

    pipenv install --dev    

Tests

    pytest /sea_dev/sea_lib_base/sealib_base/tests

Coverage

	pytest --cov /sea_dev/sea_lib_base/sealib_base/tests --cov-report=html
	
Build/Deploy Documentation

    mkdocs gh-deploy
    

### Production
None
