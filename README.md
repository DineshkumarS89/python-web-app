# python-web-app
Simple Python web app with automated test

# Steps to run the web app
1. install Flask, requests
2. Run the web app using the below command \
   nohup python app.py &
3. Logs will be written to output.log file in the same folder

# Steps to execute the automated test
 1. Run command to start the automated python test \
    python perf_test.py <No. Of Users> <TPS> <Duration in secs> \
    **Sample request** \
    python perf_test.py 10 10 300 \
 2. Sample Output \
    Home Page: Total Hits: 1500, avg response time: 0.0076, min response time: 0.0030, max response time: 0.03 \
    Submit Page: Total Hits: 1500, avg response time: 0.0082, min response time: 0.0030, max response time: 0.05
  
