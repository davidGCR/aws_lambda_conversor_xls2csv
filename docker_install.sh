virtualenv venv
source venv/bin/activate
pip3 install xlwt
cd venv/lib/python3.7/site-packages
touch __init__.py
cd ../
mv site-packages libs
zip -r deployment_package.zip .