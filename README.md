# Test deploying python pandas & fbprophet based service on AWS Lambda using Zappa & Serverless frameworks

### Deploy to serverless
`
docker run -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_DEFAULT_REGION=eu-west-1 -v $(pwd)/serverless:/var/task <your image name> bash -c "npm install serverless-python-requirements && cat requirements.txt | xargs -n 1 -L 1 pip install -I && serverless deploy && rm -r node_modules && rm package*.json"
`

### Examples for configuring a security policy for Serverless
- See https://github.com/serverless/serverless/issues/1439

### Deploy to zappa (see https://blog.zappa.io/posts/simplified-aws-lambda-deployments-with-docker-and-zappa)

`
docker run -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -e AWS_DEFAULT_REGION=eu-west-1 -v $(pwd)/zappa:/var/task <your image name> bash -c "source /var/env/bin/activate && cat requirements.txt | xargs -n 1 -L 1 pip install -I && zappa update dev"
`

### Examples for configuring a security policy for Zappa
- See https://github.com/Miserlou/Zappa/issues/244


