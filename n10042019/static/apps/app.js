

$(() =>{
     Vue.component('button-counter', {
      data: function () {
        return {
          count: 0
        }
      },
      template: '<button v-on:click="count++">Bạn đã bấm {{ count }} lần.</button>'
})
    new Vue({
        delimiters: ['${', '}'],
        el:'#SnKuz',
        data:{
            name:'Hai'

        }
    })//endvue

})