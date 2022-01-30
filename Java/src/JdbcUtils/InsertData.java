package JdbcUtils;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public class InsertData {
    public static void main(String[] args) {
        Connection conn = null;
        // Statement st = null;
        PreparedStatement pst = null;

        try {
            conn = JdbcUtils.getConnection(); // 获取数据库链接
            // String sql = "insert into perf_assess_activity(name) values('20220130act');";
            // st = conn.createStatement(); // 获得SQL的执行对象
            // int i = st.executeUpdate(sql);
            // if (i > 0) {
            //    System.out.println("新增成功");
            // }
            String sql = "insert into perf_assess_activity(name) values(?);";
            pst = conn.prepareStatement(sql);
            pst.setString(1, "20220130act");
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            JdbcUtils.release(conn, pst, null); // 释放资源
        }
    }
}
