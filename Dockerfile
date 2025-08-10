FROM node:18
WORKDIR /app
COPY services/web/package.json services/web/package-lock.json* ./ 
RUN npm ci || npm i
COPY services/web ./
EXPOSE 3000
CMD ["npm","run","dev","--","--host","0.0.0.0","--port","3000"]
