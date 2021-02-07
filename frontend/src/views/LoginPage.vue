<template>
  <div class="login">
    <div>
      <LoginForm/>
    </div>
  </div>
</template>

<script>

import LoginForm from "../components/LoginPage/LoginForm";
export default {
  name: 'login',
  components: {
    LoginForm
  }
}
</script>
