<template>
  <div class="hello">
    <img src='@/assets/logo-django.png' style="width: 250px" />
    <p>Pavilhão 1 do ASA/Prudente</p>
    <hr/>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: "Pavilhao1",
  data() {
    return {};
  },
  computed: mapState({
    messages: state => state.messages.messages
  }),
  methods: mapActions('messages', [
    'addMessage',
    'deleteMessage'
  ]),
  created() {
    this.$store.dispatch('messages/getMessages')
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
hr {
  max-width: 65%;
}

.msg {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.msg-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}

img {
  width: 250px;
  padding-top: 50px;
  padding-bottom: 50px;
}

</style>
