container_name=aws_lambda_builder
docker_image=lambdaxls
docker run -itd --name=$container_name $docker_image
docker cp ./docker_install.sh $container_name:/
docker cp ./lambda_function.py $container_name:/
docker exec $container_name bash -c "./docker_install.sh ; cp /venv/lib/python3.7/deployment_package.zip deployment_package.zip"
docker cp $container_name:/venv/lib/python3.7/deployment_package.zip deployment_package.zip
docker exec $container_name bash -c "zip -g deployment_package.zip lambda_function.py"
docker cp  $container_name:/deployment_package.zip .
docker stop $container_name
docker rm $container_name