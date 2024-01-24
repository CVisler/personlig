<template>
  <v-combobox
    v-model="chips"
    :items="items"
    chips
    clearable
    label="Select columns"
    multiple
    prepend-icon="mdi-filter-variant"
    solo
    @change="log"
  >
    <template v-slot:selection="{ attrs, item, select, selected }">
      <v-chip
        v-bind="attrs"
        :input-value="selected"
        close
        @click="select"
        @click:close="remove(item)"
      >
        <strong>{{ item }}</strong> 
      </v-chip>
    </template>
  </v-combobox>
</template>
<script>
  export default {
    data () {
      return {
        chips: ['Programming', 'Playing video games', 'Watching movies', 'Sleeping'],
        items: ['Streaming', 'Eating'],
      }
    },

    methods: {
      remove (item) {
        this.chips.splice(this.chips.indexOf(item), 1)
      },
      log (item) {
        let element = document.getElementsByClassName('yoink')
        element[0].innerHTML = item
      },
    },
  }
</script>
