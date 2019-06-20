# Testing

Tests are located in project directory folder `./sea_lib_phishlabs/tests`.

## Instructions

### Development
Select Folder

    cd /sea
    
Clone Source

    git clone -b devl git@github.info53.com:Fifth-Third/sea_lib_phishlabs.git

Virtual Environment Setup

    pipenv install --dev    

Tests

    pytest /sea/sea_lib_phishlabs/sea_lib_phishlabs/tests

Coverage

	pytest --cov /sea/sea_lib_phishlabs/sea_lib_phishlabs/tests --cov-report=html
	
Build/Deploy Documentation

    mkdocs gh-deploy
    

### Production

* None
