<template>
  <div id="background">
    <!--  <img src="../assets/loginimg.png"/>-->

    <div class="auth-form" style="margin-top: 14%">
      <h1 style="margin-bottom: 20px;text-align: center;font-size: 45px">Bridge课程系统</h1>
      <div class="auth-form-body">
        <el-form ref="form" label-width="80">
          <label>用户名</label>
          <el-input class="input-info" v-model="username" placeholder="请输入用户名"
                    prefix-icon="el-icon-user"></el-input>
          <div style="padding: 16px 0;position: relative">
            <label>密码</label>
            <el-link type="primary" style="position: absolute; top: 16px;right: 0;font-size: 14px"
                     @click="handleForgotPassword">忘记密码？
            </el-link>
            <el-input class="input-info" show-password v-model="password" placeholder="请输入密码"
                      prefix-icon="el-icon-lock"></el-input>

            <el-button type="success" style="width: 100% ;margin-top: 16px" @click="handleLogin">登录</el-button>
          </div>
        </el-form>
      </div>

      <div class="auth-form-body" style="margin-top: 16px;text-align: center;position: relative">
        <label>还没有账号？尝试去</label>
        <el-link type="primary" style="font-size: 14px;position: absolute;top: 16px" @click="dialogVisible=true">注册
        </el-link>
        <label style="margin-left: 31px">吧！</label>
      </div>

    </div>

    <el-dialog
      title="注册"
      center
      :visible.sync="dialogVisible"
      width="35%"
      :before-close="handleClose"
      append-to-body>
      <el-form ref="form" :model="registerForm" label-width="20%">
        <el-form-item label="学号">
          <el-input v-model="registerForm.student_id"></el-input>
        </el-form-item>
        <el-form-item label="姓名">
          <el-input v-model="registerForm.student_realName"></el-input>
        </el-form-item>
        <el-form-item label="邮箱">
          <el-input v-model="registerForm.student_email"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="registerForm.student_password1"></el-input>
        </el-form-item>
        <el-form-item label="请再次输入密码">
          <el-input v-model="registerForm.student_password2"></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取消</el-button>
    <el-button type="primary" @click="handleRegister">确定</el-button>
  </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  name: "Login",

  data() {
    return {
      username: "",
      password: "",

      registerForm: {
        student_id: '',
        student_password1: '',
        student_password2: '',
        student_realName: '',
        student_email: '',
      },

      dialogVisible: false,
    };

  },

  methods: {
    handleLogin() {
      if (this.check(this.username) && this.check(this.password)) {
        this.$axios.post("http://127.0.0.1:8000/app01/student/login/", {
            "student_id": this.username,
            "student_password": this.password
          }
        ).then(response => {
          console.log(response.data)

          let code = response.data.code

          if (code === 0) {
            this.$message({
                message: "登录成功！",
                type: "success"
              }
            );

            setTimeout(() => {
              this.$router.push("/main");
            }, 1000);

          } else if (code === 4002) {
            this.$alert("用户不存在", {
              type: "error",
              confirmButtonText: "确定",
              callback: action => {
                this.password = "";
                this.username = "";
              }
            })
          } else if (code === 4004) {
            this.$alert("密码不对", {
              type: "error",
              confirmButtonText: "确定",
              callback: action => {
                this.password = "";
              }
            })
          }
        }).catch(error => {
          console.log(error)
        })
      } else {
        this.$message({message: '请输入字符', type: 'warning'})
      }
    },

    handleForgotPassword() {
    },
    //TODO

    check(value) {
      return value !== '';
    },

    handleRegister() {
      if (this.check(this.registerForm.id) && this.check(this.registerForm.name)
        && this.check(this.registerForm.email) && this.check(this.registerForm.password)
        && this.check(this.registerForm.re_password)) {

        this.$axios.post('http://127.0.0.1:8000/app01/student/register/', this.registerForm).then(response => {
            console.log(response.data);

            if (response.data.error === 0) {

              this.$message({
                  message: "注册成功！",
                  type: "success"
                }
              );

              this.dialogVisible = false;
            } else {

              this.$message({
                  message: "注册失败！",
                  type: 'warning'
                }
              );
            }
          }
        ).catch(error => {
            console.log(error);
          }
        )
      } else {
        this.$message({message: '请输入字符', type: 'warning'})
      }
    },

    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
        })
        .catch(_ => {
        });
    }
  }

}
</script>

<style scoped>
#background {
  background: url("../assets/R-C.png") center center no-repeat;
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: cover;
}


.auth-form {
  width: 340px;
  margin: 0 auto;
  text-align: left;
}

.auth-form-body {
  border-radius: 6px;
  padding: 16px;
  font-size: 14px;
  background-color: #f6f8fa;
  border: 1px solid hsla(210, 18%, 87%, 1);
}

.input-info {
  padding: 5px 0;
  font-size: 14px;
}

</style>
