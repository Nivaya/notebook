package main

import (
	"fmt"
	"log"
	"net/http"
)

type Hello struct{}

func (h Hello) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.Method)
	fmt.Println(r.Host)
	fmt.Fprint(w, "Hello!")
}

func main() {
	var h Hello
	err := http.ListenAndServe("localhost:9090", h)
	if err != nil {
		log.Fatal(err)
	}
}
