<template>
  <v-bottom-navigation
    v-model="value"
    :background-color="color"
    shift
  >
    <v-btn>
      <span>TME</span>

      <v-icon>mdi-television</v-icon>
    </v-btn>

    <v-btn>
      <span>VSE</span>

      <v-icon>mdi-music-note</v-icon>
    </v-btn>

    <v-btn>
      <span>DIM</span>

      <v-icon>mdi-camera</v-icon>
    </v-btn>

    <v-btn>
      <span>MOB</span>

      <v-icon>mdi-cellphone-android</v-icon>
    </v-btn>
  </v-bottom-navigation>
</template>
