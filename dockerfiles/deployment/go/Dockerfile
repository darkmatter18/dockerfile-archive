FROM golang:alpine as builder

WORKDIR /app

RUN mkdir build

COPY . /app/

RUN go mod tidy

ENV GOOS=linux

RUN go build -o ./build/server .

FROM alpine:latest

WORKDIR /app

COPY --from=builder /app/build/ .
COPY --from=builder /app/assets/ ./assets/

EXPOSE 8080

CMD ["./server"]