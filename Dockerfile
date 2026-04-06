# --- STAGE 1: Angular compilation ---
FROM node:25 AS angular-builder
WORKDIR /build-frontend
COPY ./aira-angular/package*.json ./
RUN npm install
COPY ./aira-angular . 
# Esegue la build e genera la cartella dist
RUN npx ng build --configuration production --output-path=./dist

# --- STAGE 2: aira-express ---
FROM node:25-slim
WORKDIR /app

# Installazione dipendenze aira-express
COPY ./aira-express/package*.json ./
RUN npm install --only=production
COPY ./aira-express .

# COPIA IL COMPILATO DI ANGULAR
COPY --from=angular-builder /build-frontend/dist ./aira-angular

EXPOSE 8080
CMD ["npm", "start"]
