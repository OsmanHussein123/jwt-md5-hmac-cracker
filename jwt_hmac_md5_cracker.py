import hashlib
import hmac
import base64
import itertools
import string

def sign_jwt(payload, secret_key):
    header = '{"alg":"MD5_HMAC"}'
    
    # Encode the header and payload as base64 strings
    encoded_header = base64.urlsafe_b64encode(header.encode()).decode().rstrip('=')
    encoded_payload = base64.urlsafe_b64encode(payload.encode()).decode().rstrip('=')
    
    # Concatenate the encoded header and payload with a dot ('.')
    encoded_token = f"{encoded_header}.{encoded_payload}"
    
    # Sign the token using MD5 HMAC and the secret key
    signature = hmac.new(secret_key.encode(), encoded_token.encode(), hashlib.md5).digest()
    encoded_signature = base64.urlsafe_b64encode(signature).decode().rstrip('=')
    
    # Concatenate the encoded token and signature with a dot ('.')
    signed_token = f"{encoded_token}.{encoded_signature}"
    
    return signed_token


# Example usage
payload = '{"username":"osman"}'
print(f"test: {sign_jwt(payload, 'secret')}")

correct_token = "eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6Im9zbWFuIn0.q7cGbsBSmP67j7aJI8uChA" 

x=0
chars = string.ascii_letters + string.digits
print(chars)
for x in range(0,21):
 char=itertools.product(chars,repeat=x)
 print(x)
 for pin in char:
  pinready=''.join(pin)  
  jwt_token = sign_jwt(payload, pinready)
  print(jwt_token,pinready)
  if(jwt_token == correct_token):
    print(f"found: {jwt_token,pinready}" )
