FROM golang:alpine AS builder
WORKDIR /app
COPY / /
RUN apk add build-base && apk cache clean
RUN go build -o /app/s3-benchmark /main.go


FROM scratch
WORKDIR /app
COPY /templates ./templates
COPY --from=builder /app/s3-benchmark ./s3-benchmark
CMD ["./s3-benchmark"]