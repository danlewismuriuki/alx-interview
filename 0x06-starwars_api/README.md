# 0. Star Wars Characters

This project involves creating a Node.js script that interacts with the Star Wars API to fetch and display information about Star Wars characters from a specific movie. The movie is specified by its ID, and the script will print the names of characters associated with that movie.

## Project Overview

The goal of this project is to demonstrate your ability to work with external APIs, handle asynchronous operations in JavaScript, and manipulate command-line arguments. You will use the Star Wars API to retrieve and display character names based on the movie ID provided as an argument.

## Concepts Covered

- **HTTP Requests in JavaScript**: Making HTTP requests using the `request` module to fetch data from the Star Wars API.
- **Working with APIs**: Understanding and interacting with RESTful APIs, parsing JSON data returned by the API.
- **Asynchronous Programming**: Managing asynchronous operations with callbacks, promises, and `async/await` syntax.
- **Command Line Arguments in Node.js**: Accessing command-line arguments using `process.argv`.
- **Array Manipulation and Iteration**: Iterating over arrays and formatting data for display.

## Installation

1. **Install Node.js 10:**

    ```bash
    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    sudo apt-get install -y nodejs
    ```

2. **Install `semi-standard` for code style:**

    ```bash
    sudo npm install semistandard --global
    ```

3. **Install the `request` module:**

    ```bash
    sudo npm install request --global
    export NODE_PATH=/usr/lib/node_modules
    ```

## Usage

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd 0x06-starwars_api
    ```

2. **Make the script executable:**

    ```bash
    chmod +x 0-starwars_characters.js
    ```

3. **Run the script with a movie ID:**

    ```bash
    ./0-starwars_characters.js <movie-id>
    ```

    Replace `<movie-id>` with the desired movie ID. For example, `3` for "Return of the Jedi".

## Example

To fetch and display characters from the movie with ID `3`, use the following command:

```bash
./0-starwars_characters.js 3

