package JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public class DeleteData {
    public static void main(String[] args) {
        Connection conn = null;
        // Statement st = null;
        PreparedStatement pst = null;

        try {
            conn = JdbcUtils.getConnection(); // 获取数据库链接
            // st = conn.createStatement(); // 获得SQL的执行对象
            // String sql = "delete from perf_assess_activity where name like '%act';";
            // int i = st.executeUpdate(sql);
            // if (i > 0) {
            //     System.out.println("删除成功");
            // }
            String sql = "delete from perf_assess_activity where name like ？;";
            pst = conn.prepareStatement(sql);
            pst.setString(1, "%act");
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(conn, pst, null); // 释放资源
        }
    }
}
