<template>
  <div class="hello">
    <h1>{{ message }}</h1>
		<div v-html="htmlMessage"></div>

		<div :id="hi" name="hello" :class="classHello">
			qqqqq
		</div>

		<div v-if="boolMessage">
			if true print
		</div>
		<div v-else>
			if false print
		</div>

		<div v-show="showMessage">
			showMessage
		</div>

		<div v-for="item in listMessage">
			{{item}}
		</div>

		<el-button onclick='alert(1)'>纯jsbutton</el-button>
		<el-button @click='buttonEvent'>Vuebutton</el-button>

		<el-input v-model="inputMessage"/>
		<div>
				{{inputMessage}}
		</div>

		<el-button @click='inputEvent'>inputEvent</el-button>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      message: 'hi xiaoweide',
			htmlMessage:"<span style='color:red'> hi weide</span>",
			hi:"hiHelloWorld",
			classHello:"hiHelloWorld",

			boolMessage:false,
			showMessage:false,

			listMessage: ['a', 'b', 'c'],

			inputMessage: "input"
    }
  },
	methods: {
		buttonEvent(){
			this.showMessage = !this.showMessage
		},
		inputEvent(){
			this.inputMessage = "input"
		}
	}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.hiHelloWorld {
	color: blue;
}
</style>
