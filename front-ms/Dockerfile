FROM node:lts-alpine as build-stage
WORKDIR /frontend
COPY package*.json /frontend/
RUN yarn install
COPY . /frontend/
RUN yarn build

FROM nginx:latest
COPY --from=build-stage /frontend/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 443
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
