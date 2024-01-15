<template>
  <v-sheet
    class="overflow-hidden"
  >
    <v-container class="fill-height">
      <v-row
      >
        <v-btn 
          class="main-nav-btn"
          dark
          @click.stop="drawer = !drawer"
        >
          <v-icon 
            dark
          >mdi-menu
          </v-icon>
        </v-btn>
      </v-row>
    </v-container>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list-item>

        <v-list-item-content>
          <v-list-item-title>navigation</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :href="item.link"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-sheet>
</template>
<link rel="stylesheet" type="text/css" href="assets/style.css" />
<script>
  export default {
    data () {
      return {
        drawer: null,
        items: [
          { title: 'Home', icon: 'mdi-home', link: '/' },
          { title: 'TV', icon: 'mdi-television', link: '/TME' },
          { title: 'Sound', icon: 'mdi-speaker', link: '/VSE'},
          { title: 'DI', icon: 'mdi-camera', link: '/DIM'},
          { title: 'MOB', icon: 'mdi-cellphone', link: '/MOB'},
          { title: 'File drop', icon: 'mdi-upload', link: '/'},
        ],
      }
    },
  }
</script>
