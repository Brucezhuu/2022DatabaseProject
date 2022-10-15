<template>
  <div>
    <img src="../assets/school.png" width="400" height="100">

    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        label="课程代号"
        prop="course_id">
      </el-table-column>

      <el-table-column
        label="课程名称"
        prop="course_name">
      </el-table-column>

      <el-table-column
        label="授课老师"
        prop="course_teacher_name">
      </el-table-column>

      <el-table-column
        label="课程信息"
        prop="course_info">
      </el-table-column>

      <el-table-column
        label="上课时间"
        prop="course_time">
      </el-table-column>

      <el-table-column
        align="right">
        <template slot="header" slot-scope="scope">
          <el-button type="success" @click="dialogVisible=true">
            添加
          </el-button>
        </template>
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑
          </el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除
          </el-button>
        </template>
      </el-table-column>

    </el-table>

    <el-dialog
      title="添加课程"
      center
      :visible.sync="dialogVisible"
      width="35%"
      :before-close="handleClose"
      append-to-body>
      <el-form ref="form" :model="addFrom" label-width="20%">
        <el-form-item label="课程代码">
          <el-input v-model="addFrom.course_id"></el-input>
        </el-form-item>
        <el-form-item label="课程名称">
          <el-input v-model="addFrom.course_name"></el-input>
        </el-form-item>
        <el-form-item label="授课老师">
          <el-input v-model="addFrom.course_teacher_name"></el-input>
        </el-form-item>
        <el-form-item label="课程信息">
          <el-input v-model="addFrom.course_info"></el-input>
        </el-form-item>
        <el-form-item label="上课时间">
          <el-input v-model="addFrom.course_time"></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisible = false">取消</el-button>
    <el-button type="primary" @click="handleAdd">确定</el-button>
  </span>
    </el-dialog>

    <el-dialog
      title="编辑课程"
      center
      :visible.sync="dialogVisibleEdit"
      width="35%"
      :before-close="handleClose"
      append-to-body>
      <el-form ref="form" :model="editFrom" label-width="20%">
        <el-form-item label="课程代码">
          <el-input v-model="editFrom.course_id" disabled></el-input>
        </el-form-item>
        <el-form-item label="课程名称">
          <el-input v-model="editFrom.course_name"></el-input>
        </el-form-item>
        <el-form-item label="授课老师">
          <el-input v-model="editFrom.course_teacher_name"></el-input>
        </el-form-item>
        <el-form-item label="课程信息">
          <el-input v-model="editFrom.course_info"></el-input>
        </el-form-item>
        <el-form-item label="上课时间">
          <el-input v-model="editFrom.course_time"></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
    <el-button @click="dialogVisibleEdit = false">取消</el-button>
    <el-button type="primary" @click="handleEditSubmit">确定</el-button>
  </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  name: "Main",

  data() {

    return {
      tableData: [],
      addFrom: {
        course_id: '',
        course_name: '',
        course_department: '',
        course_teacher_id: '',
        course_teacher_name: '',
        course_info: '',
        course__pc: '',
        course_count: '',
        course_time: '',
        course_total: '',
      },
      editFrom: [{
        course_id: '',
        course_name: '',
        course_teacher_name: '',
        course_info: '',
        course_time: '',
      }],
      editInfo: 0,
      dialogVisible: false,
      dialogVisibleEdit: false,
    }
  },

  created() {
    this.$axios.get('http://127.0.0.1:8000/app01/course/').then(response => {
      console.log(response)

      this.tableData = response.data.data
      // var data = response.data.data;
      //
      // for (var i = 0; i < 6; i++) {
      //   this.tableData.push(data[i])
      //   console.log(data[i])
      // }
    })
  }
  ,

  methods: {

    handleEdit(index, row) {
      console.log(index, row);

      this.dialogVisibleEdit = true;
      this.editFrom = {...row}
      this.editInfo = index
      console.log(this.editInfo)
    }
    ,
    handleDelete(index, row) {
      console.log(index, row);

      this.$axios.post('http://127.0.0.1:8000/app01/course/delete/', row).then(response => {
        console.log(response.data);

        if (response.data.error === 0) {
          this.tableData.splice(index, 1);
          this.$msgbox({
            message: '删除成功',
            type: 'success'
          })
        } else {
          this.$message({message: '删除失败', type: 'error'})
        }
      })

    }
    ,
    handleAdd() {
      console.log(this.addFrom)
      this.$axios.post('http://127.0.0.1:8000/app01/course/add/', this.addFrom).then(response => {

        if (response.data.error === 0) {

          this.$msgbox({
            message: '添加成功',
            type: 'success'
          })

          this.tableData.push(this.addFrom)
          console.log(this.tableData)
          this.dialogVisible = false;

        } else {
          this.$message({message: '添加失败', type: 'error'})
        }
      })

    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
        })
        .catch(_ => {
        });
    },
    handleEditSubmit() {
      this.$axios.post('http://127.0.0.1:8000/app01/course/edit/', this.editFrom).then(response => {
        console.log(response.data);

        if (response.data.error === 0) {
          this.tableData.splice(this.editInfo, 1, this.editFrom);
          console.log(this.editInfo)

          this.$msgbox({
            message: '修改成功',
            type: 'success'
          })

          this.dialogVisibleEdit = false;

        } else {
          this.$message({message: '添加失败', type: 'error'})
        }
      })

    },
  }
  ,
}
</script>


<style scoped>

</style>
