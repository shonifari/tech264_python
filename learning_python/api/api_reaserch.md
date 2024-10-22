
# API Research

## What are APIs? How are they used and why are they so popular?

An API, or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate with each other. APIs are used to enable the integration of various services and functionalities, allowing developers to build complex systems more efficiently by leveraging existing components. They are popular because they:

- Simplify and accelerate development by allowing reuse of existing services.
- Enable interoperability between different systems and platforms.
- Enhance security by exposing only necessary data and functionalities.
- Support scalability and flexibility in software design.

## What is a REST API? What makes an API RESTful? What are the REST guidelines?

A REST API (Representational State Transfer API) is an architectural style for designing networked applications. It relies on a stateless, client-server communication protocol, usually HTTP. An API is considered RESTful if it adheres to the following principles:

1. **Uniform Interface**: Ensures consistent and predictable interactions.
2. **Client-Server**: Separates client and server concerns.
3. **Stateless**: Each request from client to server must contain all the information needed to understand and process the request.
4. **Cacheable**: Responses must define themselves as cacheable or not to prevent clients from reusing stale data.
5. **Layered System**: Allows an architecture to be composed of hierarchical layers by constraining component behavior.
6. **Code on Demand (optional)**: Servers can extend client functionality by transferring executable code.

## What is HTTP? What is HTTPS?

HTTP stands for HyperText Transfer Protocol. It is used for transmitting hypertext requests and information on the internet. HTTPS is the secure version of HTTP, where the 'S' stands for Secure. HTTPS uses encryption protocols like TLS (Transport Layer Security) to secure data transfer between the client and server.

## HTTP Request Structure

An HTTP request consists of:

- **Request Line**: Contains the HTTP method, the resource URL, and the HTTP version.
- **Headers**: Provide additional information about the request.
- **Body**: Contains the data to be sent to the server (used with methods like POST and PUT).

Example:
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

## HTTP Response Structure

An HTTP response consists of:

- **Status Line**: Contains the HTTP version, status code, and status message.
- **Headers**: Provide additional information about the response.
- **Body**: Contains the data sent back to the client.

Example:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 138

<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>
```

## What are the 5 HTTP verbs and what do they do?

- **GET**: Retrieves data from the server.
- **POST**: Sends data to the server to create a new resource.
- **PUT**: Updates an existing resource with new data.
- **PATCH**: Partially updates an existing resource.
- **DELETE**: Deletes a specified resource.

## What is statelessness? Examples of Stateless and Stateful HTTP Requests

Statelessness means that each request from a client to a server must contain all the information needed to understand and process the request. The server does not store any state about the client session.

**Stateless Request Example**:
```
GET /user/123 HTTP/1.1
Host: www.example.com
Authorization: Bearer <token>
```

**Stateful Request Example**:
```
GET /user/123 HTTP/1.1
Host: www.example.com
Cookie: sessionId=abc123
```

## What is caching?

Caching is the process of storing copies of files or data in a cache, or temporary storage location, so that they can be accessed more quickly. In the context of web APIs, caching can significantly improve performance by reducing the need to repeatedly fetch the same data from the server.

---
