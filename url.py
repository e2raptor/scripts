 #!/usr/bin/python
import base64
import pprint
pp = pprint.PrettyPrinter(indent=4)
url = 'https://pubsdk.zoomdata.com:9443/vis/eyJzb3VyY2UiOiJUaWNrZXQgTWFya2V0cGxhY2UgRnVzaW9uIiwiY2hhcnQiOiJCYXJzIiwiY29sb3JTZXQiOnsiTXVsdGkgR3JvdXAgQnkiOiJab29tU2VxdWVudGlhbCIsIk1ldHJpYyI6Ilpvb21TZXF1ZW50aWFsIiwiQmFyIENvbG9yIjoiWm9vbVNlcXVlbnRpYWwifSwidmFyaWFibGVzIjoie1wiTXVsdGkgR3JvdXAgQnlcIjpbe1wibmFtZVwiOlwiZXZlbnRpZFwiLFwibGltaXRcIjo1MCxcInNvcnRcIjp7XCJkaXJcIjpcImFzY1wiLFwibmFtZVwiOlwiZXZlbnRpZFwifSxcImZvcm1cIjpcImV2ZW50aWRcIixcImxhYmVsXCI6XCJFdmVudFwiLFwidHlwZVwiOlwiQVRUUklCVVRFXCIsXCJmb3Jtc1wiOlt7XCJmb3JtXCI6XCJldmVudGlkXCIsXCJtYXBwaW5nXCI6W1widGlja2V0X3NhbGVzX3RhYmxlX2Z1c2lvbi5ldmVudGlkXCIsXCJteXNxbF9ldmVudHNfZnVzaW9uLmV2ZW50aWRcIl0sXCJ1bmlxdWVcIjpbXCJteXNxbF9ldmVudHNfZnVzaW9uLmV2ZW50aWRcIl0sXCJwcmltYXJ5XCI6dHJ1ZSxcInZpc2libGVcIjp0cnVlLFwibGFiZWxcIjpcIklEXCJ9LHtcImZvcm1cIjpcImV2ZW50bmFtZVwiLFwibWFwcGluZ1wiOltcIm15c3FsX2V2ZW50c19mdXNpb24uZXZlbnRuYW1lXCJdLFwidW5pcXVlXCI6W10sXCJwcmltYXJ5XCI6ZmFsc2UsXCJ2aXNpYmxlXCI6dHJ1ZSxcImxhYmVsXCI6XCJOYW1lXCJ9XX1dLFwiTWV0cmljXCI6XCJ0aWNrZXRfc2FsZXNfdGFibGVfZnVzaW9uLnNhbGVzaWQ6c3VtXCIsXCJCYXIgQ29sb3JcIjpcInRpY2tldF9zYWxlc190YWJsZV9mdXNpb24uc2FsZXNpZDpzdW1cIn0iLCJmaWx0ZXJzIjpbXSwidGltZUZpbHRlciI6eyJ0aW1lRmllbGQiOiJ0aWNrZXRfc2FsZXNfdGFibGVfZnVzaW9uLnNhbGV0aW1lIiwiZnJvbSI6IisyMDA4LTAxLTAxIDAxOjAwOjAwLjAwMCIsInRvIjoiKzIwMDgtMTItMzEgMTI6NTg6MDAuMDAwIn19'

code = url.split('/vis/')[1]

obj = base64.b64decode(code).decode(encoding='UTF-8')
obj = obj.replace('false','False')
obj = obj.replace('null','None')
obj = obj.replace('true','True')
obj = eval(obj)
obj = eval(obj['variables'])
pp.pprint(obj)



