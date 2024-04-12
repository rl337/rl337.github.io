# Use the official Ruby base image
FROM ruby:latest

# Label the image
LABEL maintainer="yourname@example.com"

# Install build dependencies and Jekyll
RUN apt-get update -qq && apt-get install -y nodejs build-essential

# Install Jekyll and Bundler
RUN gem install jekyll bundler

# Set the default directory inside the container
WORKDIR /srv/jekyll

RUN chmod a+rwx /srv/jekyll

# Set Jekyll as the default entrypoint (this lets you use any jekyll command)
ENTRYPOINT ["jekyll"]

# By default, just show the help menu (when no parameters are passed)
CMD ["--help"]
