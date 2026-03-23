import numpy as np

def calculate_atomic_z_range(lammps_file):
    """解析LAMMPS结构文件，计算原子Z坐标范围"""
    z_coords = []
    in_atoms_section = False
    
    with open(lammps_file, 'r') as f:
        for line in f:
            # 跳过注释行和空行
            if line.startswith('#') or not line.strip():
                continue
                
            # 检测原子数据段开始
            if 'Atoms' in line:
                in_atoms_section = True
                continue
                
            # 收集原子坐标
            if in_atoms_section:
                data = line.split()
                # 确保有足够的列数包含坐标数据
                if len(data) >= 5:  
                    try:
                        # z坐标在第五列（索引4）
                        z_coords.append(float(data[4]))
                    except ValueError:
                        # 忽略无法转换为浮点数的行
                        continue
    
    if not z_coords:
        raise ValueError("未找到原子坐标数据")
    
    z_min = min(z_coords)
    z_max = max(z_coords)
    z_delta = z_max - z_min
    
    return z_max, z_min, z_delta

# 使用示例
if __name__ == "__main__":
    lammps_file = "data.1"  # 当前目录下的文件
    
    try:
        z_max, z_min, z_delta = calculate_atomic_z_range(lammps_file)
        
        # 竖排输出结果，保留8位小数
        print(f"{z_max:.8f}")
        print(f"{z_min:.8f}")
        print(f"{z_delta:.8f}")
        
    except FileNotFoundError:
        print(f"错误: 文件 {lammps_file} 不存在")
    except ValueError as e:
        print(f"错误: {str(e)}")
    except Exception as e:
        print(f"未知错误: {str(e)}")