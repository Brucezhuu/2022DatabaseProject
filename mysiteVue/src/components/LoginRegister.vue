<template>
  <div>
    <div>
      <span @click="type=0">登录</span>
      <span @click="type=1">注册</span>
    </div>

    <div v-if="type===0">
      <input v-model="username" type="text" placeholder="请输入用户名">
      <input v-model="password" type="password" placeholder="请输入密码">

      <button>登录</button>
    </div>




    <div v-show="type===1">
      <input v-model="username" type="text" placeholder="手机号码">
      <input v-model="password" type="text" placeholder="短信验证码">
    </div>
  </div>


</template>

<script>
export default {
  name: "LoginRegister",

  data() {
    return {
      type: 0,
      username: "",
      password: "",
    }
  }
}
</script>

<style scoped>

</style>
