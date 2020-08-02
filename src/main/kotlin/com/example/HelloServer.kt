package com.example

import io.grpc.Server
import io.grpc.ServerBuilder

fun main() {
}


class HelloServer constructor(private val port:Int){
    val server: Server = ServerBuilder
        .forPort(port)
        .build()


}